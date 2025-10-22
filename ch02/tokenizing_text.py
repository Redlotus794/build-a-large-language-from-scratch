import os
import urllib.request
from typing import Optional


def read_verdict(file_path: Optional[str] = None, encoding: str = "utf-8") -> str:
	"""Read and return the contents of `the-verdict.txt`.

	If `file_path` is None, the function will look for `the-verdict.txt` in the
	same directory as this module (`ch02/the-verdict.txt`). The function will
	attempt to decode using `encoding` and fall back to common alternatives on
	failure.

	Returns the full file contents as a string.
	"""
	if file_path is None:
		base_dir = os.path.dirname(__file__)
		file_path = os.path.join(base_dir, "the-verdict.txt")

	# Try the requested encoding first, then fall back to latin-1 and finally
	# to utf-8 with replacement to ensure we always return a string.
	try:
		with open(file_path, "r", encoding=encoding) as f:
			return f.read()
	except FileNotFoundError:
		raise
	except UnicodeDecodeError:
		# Try latin-1 which will always succeed but may produce incorrect
		# characters for non-latin text.
		try:
			with open(file_path, "r", encoding="latin-1") as f:
				return f.read()
		except UnicodeDecodeError:
			# As a last resort, read as binary and decode with replacement
			with open(file_path, "rb") as f:
				return f.read().decode("utf-8", errors="replace")


if __name__ == "__main__":
	# Quick CLI for manual verification: print first 20 lines and file size.
	try:
		text = read_verdict()
	except FileNotFoundError:
		print("the-verdict.txt not found in the ch02 directory.\nProvide a path as an argument in the script if needed.")
	else:
		# lines = text.splitlines()
		# preview_lines = 20
		# print(f"Read {len(text)} characters ({len(lines)} lines). Showing first {min(preview_lines, len(lines))} lines:\n")
		# for i, ln in enumerate(lines[:preview_lines], start=1):
		# 	print(f"{i:3d}: {ln}")
		print(len(text))

