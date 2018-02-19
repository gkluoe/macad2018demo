# Copyright 2018 Geoff Lee
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""The macad2018demo tool"""
import argparse

VERSION = "0.0.1"
DESCRIPTION = """This is the macad2018demo tool"""

def main():
    """Main function - do useful stuff here!"""
    args = process_args()

    # Now do stuff!
    assert args

def process_args(argv=None):
    """Process any commandline arguments"""
    parser = argparse.ArgumentParser(description=DESCRIPTION,
                                     version=VERSION)
    args = parser.parse_args(argv)
    return args

if __name__ == "__main__":
    main()
