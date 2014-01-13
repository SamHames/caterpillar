# caterpillar - Compare the performance of RAM with SQL storage
#
# Copyright (C) 2012-2013 Mammoth Labs
# Author: Kris Rogers <kris@mammothlabs.com.au>
import csv
import os
import time

from caterpillar.analytics.influence import InfluenceAnalyticsPlugin
from caterpillar.data.sqlite import SqliteStorage, SqliteMemoryStorage
from caterpillar.processing.analysis.analyse import DefaultAnalyser
from caterpillar.processing.index import Index
from caterpillar.processing.schema import Schema, CATEGORICAL_TEXT, NUMERIC, TEXT


with open(os.path.abspath('caterpillar/resources/moby.txt'), 'r') as f:
    data = f.read()

# Memory Storage
ram_start = time.time()
index = Index.create(Schema(text=TEXT(analyser=DefaultAnalyser()),
                            document=TEXT(analyser=DefaultAnalyser(), indexed=False)),
                     storage_cls=SqliteMemoryStorage)
index.add_document(text=data, document='moby.txt', frame_size=2, fold_case=True, update_index=True)
index.run_plugin(InfluenceAnalyticsPlugin, influence_factor_smoothing=False)
topical_classification = InfluenceAnalyticsPlugin(index).get_topical_classification(influence_threshold=3.841)
ram_latency = time.time() - ram_start

# Sqlite
sql_start = time.time()
index = Index.create(Schema(text=TEXT(analyser=DefaultAnalyser()),
                            document=TEXT(analyser=DefaultAnalyser(), indexed=False)),
                     storage_cls=SqliteStorage, path=os.getcwd())
index.add_document(text=data, document='moby.txt', frame_size=2, fold_case=True, update_index=True)
index.run_plugin(InfluenceAnalyticsPlugin, influence_factor_smoothing=False)
topical_classification = InfluenceAnalyticsPlugin(index).get_topical_classification(influence_threshold=3.841)
sql_latency = time.time() - sql_start
index.destroy()

print 'Ram time: {}s\nSQL time: {}s'.format(ram_latency, sql_latency)

"""
import cProfile, StringIO, pstats
pr = cProfile.Profile()
pr.enable()
with open(os.path.abspath('caterpillar/resources/nps_medium.csv'), 'rbU') as f:
    index = Index.create(Schema(respondant=NUMERIC, region=CATEGORICAL_TEXT(indexed=True),
                                store=CATEGORICAL_TEXT(indexed=True),
                                liked=TEXT, disliked=TEXT, would_like=TEXT, nps=NUMERIC(indexed=True)),
                         storage_cls=SqliteStorage, path=os.getcwd())
    csv_reader = csv.reader(f)
    csv_reader.next()  # Skip header
    for row in csv_reader:
        index.add_document(update_index=False, respondant=row[0], region=row[1], store=row[2], liked=row[3],
                           disliked=row[4], would_like=row[5], nps=row[6])

    index.reindex()

#filtered_index = DerivedIndex.create_from_composite_query((index, "nps>=8"))
#filtered_index.run_plugin(InfluenceAnalyticsPlugin)
pr.disable()
index.destroy()
s = StringIO.StringIO()
sortby = 'cumulative'
ps = pstats.Stats(pr, stream=s).sort_stats(sortby)
ps.print_stats()
print s.getvalue()
"""