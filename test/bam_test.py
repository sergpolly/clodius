from __future__ import print_function

import clodius.tiles.bam as ctb
import os.path as op
import unittest

testdir = op.realpath(op.dirname(__file__))

class MyTestCase(unittest.TestCase):
    def test_tileset_info(self):
        filename_matched = op.join(
            'data',
            'SRR1770413.sorted.short.bam'
        )

        filename_mismatched = op.join(
            'data',
            'SRR1770413.mismatched_bai.bam'
        )

        tsinfo = ctb.tileset_info(filename_matched)
        assert 'max_zoom' in tsinfo

        tsinfo = ctb.tileset_info(filename_mismatched)
        assert 'max_zoom' in tsinfo

    def test_tiles(self):
        filename_matched = op.join(
            'data',
            'SRR1770413.sorted.short.bam'
        )

        filename_mismatched = op.join(
            'data',
            'SRR1770413.mismatched_bai.bam'
        )

        index_filename = op.join(
            'data',
            'SRR1770413.different_index_filename.bai'
        )

        tile = ctb.tiles(filename_matched, ['x.9.0'])

        assert len(tile) > 0

        # missing index
        self.assertRaises(ValueError, ctb.tiles, filename_mismatched, ['x.9.0'] )

        tile = ctb.tiles(filename_mismatched,
            ['x.9.0'], index_filename=index_filename)
        assert(len(tile)) > 0
