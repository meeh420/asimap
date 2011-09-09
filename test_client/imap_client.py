#!/usr/bin/env python
#
# File: $Id$
#
"""
A simplistic IMAP test client to use against our server.
"""

# system imports
#
import imaplib
import optparse

############################################################################
#
def setup_option_parser():
    """
    This function uses the python OptionParser module to define an option
    parser for parsing the command line options for this script. This does not
    actually parse the command line options. It returns the parser object that
    can be used for parsing them.
    """
    parser = optparse.OptionParser(usage = "%prog [options]",
                                   version = asimap.__version__)

    parser.set_defaults(port = 993, interface = "0.0.0.0", tls = True)

    parser.add_option("--port", action="store", type="int", dest="port",
                      help = "What port to listen on.")
    parser.add_option("--interface", action="store", type="string",
                      dest="interface", help = "The IP address to bind to.")
    parser.add_option("--no_tls", action="store_false", dest="tls",
                      help="Turn off TLS/SSL for the incoming IMAP4 "
                      "connections.")
    return parser

#############################################################################
#
def main():
    """
    Parse options.. connect to the IMAP server.. do some commands.
    """

    parser = setup_option_parser()
    (options, args) = parser.parse_args()

    return

############################################################################
############################################################################
#
# Here is where it all starts
#
if __name__ == "__main__":
    main()
#
#
############################################################################
############################################################################
