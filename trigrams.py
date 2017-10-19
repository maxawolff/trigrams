"""Kata fourteen."""


def processes_input(source_file):
	"""."""
	import io
	f = io.open(source_file, encoding='utf-8')
	source_txt = f.read()
	f.close()
print (source_txt)
return source_txt