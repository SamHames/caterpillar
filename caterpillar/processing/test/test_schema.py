# caterpillar: Tests for the caterpillar.processing.schema module
#
# Copyright (C) 2012-2013 Mammoth Labs
# Author: Kris Rogers <kris@mammothlabs.com.au>
import os

from caterpillar.processing import schema


def test_generate_schema_small():
    """Test generation of schema for small CSV file."""
    with open(os.path.abspath('caterpillar/resources/test_small.csv'), 'rbU') as f:
        csv_schema, sample_rows = schema.generate_csv_schema(f)

        assert csv_schema[3].type ==  csv_schema[4].type ==  schema.ColumnDataType.TEXT
        assert len(csv_schema) == 7


def test_generate_csv_schema_twitter():
    """Test generation of schema for twitter CSV file."""
    with open(os.path.abspath('caterpillar/resources/twitter_sentiment.csv'), 'rbU') as f:
        csv_schema, sample_rows = schema.generate_csv_schema(f)

        assert csv_schema[0].name == 'Sentiment'
        assert csv_schema[0].type == schema.ColumnDataType.IGNORE
        assert csv_schema[1].name == 'Text'
        assert csv_schema[1].type == schema.ColumnDataType.TEXT
