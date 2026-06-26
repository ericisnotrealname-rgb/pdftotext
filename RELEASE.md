This document details the release process.

1. Commit updated versions of `CHANGES.md` and `pyproject.toml`
2. Make sure the directory is clean: `git status` shows nothing
3. Create a new virtual environment with `twine` and `build`
4. Run `python -m build`
5. Ask twine how it looks: `twine check --strict dist/*`
6. Manually verify what's in the tarball: `tar --list --file dist/pdftotext-X.X.X.tar.gz`
7. Upload to test PyPI: `twine upload --repository testpypi dist/pdftotext-X.X.X.tar.gz`
8. If it looks good there, upload to real PyPI: `twine upload dist/pdftotext-X.X.X.tar.gz`
9. Tag the release on our git host
