# Copyright 1999-2009 Gentoo Foundation
# Distributed under the terms of the GNU General Public License v2
# $Id$

from __future__ import print_function

import sys

from portage.output import bold, create_color_func

def userquery(prompt, responses=None, colours=None):
	"""Displays a prompt and a set of responses, then waits for a response
	which is checked against the responses and the first to match is
	returned.  An empty response will match the first value in responses.  The
	input buffer is *not* cleared prior to the prompt!

	prompt: a String.
	responses: a List of Strings.
	colours: a List of Functions taking and returning a String, used to
	process the responses for display. Typically these will be functions
	like red() but could be e.g. lambda x: "DisplayString".
	If responses is omitted, defaults to ["Yes", "No"], [green, red].
	If only colours is omitted, defaults to [bold, ...].

	Returns a member of the List responses. (If called without optional
	arguments, returns "Yes" or "No".)
	KeyboardInterrupt is converted to SystemExit to avoid tracebacks being
	printed."""
	if responses is None:
		responses = ["Yes", "No"]
		colours = [
			create_color_func("PROMPT_CHOICE_DEFAULT"),
			create_color_func("PROMPT_CHOICE_OTHER")
		]
	elif colours is None:
		colours=[bold]
	colours=(colours*len(responses))[:len(responses)]
	print(bold(prompt), end=' ')
	try:
		while True:
			response=raw_input("["+"/".join([colours[i](responses[i]) for i in range(len(responses))])+"] ")
			for key in responses:
				# An empty response will match the first value in responses.
				if response.upper()==key[:len(response)].upper():
					return key
			print("Sorry, response '%s' not understood." % response, end=' ')
	except (EOFError, KeyboardInterrupt):
		print("Interrupted.")
		sys.exit(1)

