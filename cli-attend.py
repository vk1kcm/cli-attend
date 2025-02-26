#!/usr/bin/env python3
#
# cli-attend
# A command line simple search, mark and output inot a csv file an attendance register
#
# Carl Makin

import argparse
import re

parser = argparse.ArgumentParser()
parser.add_argument("members", help="List of members in csv format")
parser.add_argument("attendees", help="File to store attending members")
args = parser.parse_args()

memberfile = open(args.members, "r")
attendeefile = open(args.attendees, "a")

members = memberfile.readlines()
memberfile.close()

query = ""

while (True):
    print("")
    query = input("Search for: ")
    if (query == "q"):
        break
    for i in range(len(members)):
        result = re.search(query, members[i], re.IGNORECASE)
        if result:
            print("(", i, ") ", members[i])

    r = input("Enter number of found attendee (or <enter> if not found): ")
    if (r !=""):
        rpos = int(r)
        attendeefile.write(members[rpos])
        print(members[rpos].rstrip(), "marked as attending.")

attendeefile.close()


