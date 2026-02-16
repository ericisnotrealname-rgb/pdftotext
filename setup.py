import setuptools

# This includes extra paths for brew on macOS
module = setuptools.Extension(
    "pdftotext",
    sources=["pdftotext.cpp"],
    libraries=["poppler-cpp"],
    include_dirs=["/opt/homebrew/include", "/usr/local/include"],
    library_dirs=["/opt/homebrew/lib", "/usr/local/lib"],
    extra_compile_args=["-std=c++11", "-Wall"],
)

with open("README.md") as f:
    long_description = f.read()

setuptools.setup(
    name="pdftotext",
    version="3.0.0",
    author="Jason Alan Palmer",
    author_email="jalanpalmer@gmail.com",
    description="Simple PDF text extraction",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/jalan/pdftotext",
    license="MIT",
    ext_modules=[module],
)
