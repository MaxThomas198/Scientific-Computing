#!/usr/bin/python

#################################################
# module: poly_parser.py
# bugs to vladimir dot kulyukin in canvas
#################################################
from maker import maker
import re


class poly_parser(object):

    @staticmethod
    def parse_elt(elt):
        # let's make sure that elt is a string.
        assert isinstance(elt, str)
        els = re.split('([a-zA-Z^])', elt)
        const = float(els[0])
        exp = float(els[4])
        poly = maker.make_prod(maker.make_const(const),
                               maker.make_pwr(els[1], exp))
        return poly

    @staticmethod
    def parse_sum(poly_str):
        assert isinstance(poly_str, str)
        indelms = poly_str.split()
        for i in range(len(indelms)):
            if indelms[i] == '-':
                indelms[i] = '+'
                indelms[i + 1] = '-' + indelms[i + 1]
        try:
            while True:
                indelms.remove('+')
        except ValueError:
            pass
        print(len(indelms))
        if len(indelms) == 1:
            return poly_parser.parse_elt(poly_str)
        else:
            parse_sum = maker.make_plus(poly_parser.parse_elt(indelms[0]), poly_parser.parse_elt(indelms[1]))
        for i in range(2, len(indelms)):
            parse_sum = maker.make_plus(parse_sum, poly_parser.parse_elt(indelms[i]))
        return parse_sum

        # if totalcnt == 1:
        #     return maker.make_plus(poly_parser.parse_elt(indelms[0]), poly_parser.parse_elt(indelms[2]))
        # if totalcnt == 2:
        #     return maker.make_plus(maker.make_plus(poly_parser.parse_elt(indelms[0]), poly_parser.parse_elt(indelms[2]))
        #                            , poly_parser.parse_elt(indelms[4]))
        # if totalcnt == 3:
        #     return maker.make_plus(maker.make_plus(maker.make_plus(poly_parser.parse_elt(indelms[0]),
        #                                                            poly_parser.parse_elt(indelms[2]))
        #                                            , poly_parser.parse_elt(indelms[4])),
        #                            poly_parser.parse_elt(indelms[6]))
        # if totalcnt == 4:
        #     return maker.make_plus(maker.make_plus(maker.make_plus(maker.make_plus(poly_parser.parse_elt(indelms[0]),
        #                                                                            poly_parser.parse_elt(indelms[2]))
        #                                                            , poly_parser.parse_elt(indelms[4])),
        #                                            poly_parser.parse_elt(indelms[6])),
        #                            poly_parser.parse_elt(indelms[8]))
