#!/usr/bin/env python3
import os
import singer
from singer import utils


class IDS(object):
    BUSINESS_UNITS = "business_units"
    REVIEWS = "reviews"
    CONSUMERS = "consumers"

stream_ids = [getattr(IDS, x) for x in dir(IDS)
              if not x.startswith("__")]

PK_FIELDS = {
    IDS.BUSINESS_UNITS: ["id"],
    IDS.REVIEWS: ["business_unit_id", "id"],
    IDS.CONSUMERS: ["id"],
}


def get_abs_path(path):
    return os.path.join(os.path.dirname(os.path.realpath(__file__)), path)


def load_schema(tap_stream_id):
    path = "schemas/{}.json".format(tap_stream_id)
    return utils.load_json(get_abs_path(path))


def load_and_write_schema(tap_stream_id):
    schema = load_schema(tap_stream_id)
    singer.write_schema(tap_stream_id, schema, PK_FIELDS[tap_stream_id])
