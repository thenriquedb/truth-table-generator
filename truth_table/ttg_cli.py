#!/usr/bin/env python

"""
CLI for the truth_table_generator package.
"""

# Copyright 2019 Francisco Bustamante
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.

# Package forked from truths, a module by Trey Morris

import argparse
import ast
import truth_table


def clielement():
    """
    CLI for the truth_table_generator package.
    """

    parser = argparse.ArgumentParser()
    parser.add_argument('variables',
                        help="List of variables e. g. \"['p', 'q']\"")
    parser.add_argument('-p', '--propositions',
                        help="List of propositions e. g. \"['p or q', 'p and q']\"")
    parser.add_argument('-i', '--ints', default='True',
                        help='True for 0 and 1; False for words')
    args = parser.parse_args()

    variables = ast.literal_eval(args.variables)
    ints = ast.literal_eval(args.ints)

    print()
    if args.propositions is None:
        propositions = []
        print(truth_table.Truths(variables, propositions, ints))
    else:
        propositions = ast.literal_eval(args.propositions)
        print(truth_table.Truths(variables, propositions, ints))
    print()


if __name__ == "__main__":
    clielement()
