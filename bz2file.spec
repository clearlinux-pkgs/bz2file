#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xF5AA16828D5E4230 (nadeem.vawda@gmail.com)
#
Name     : bz2file
Version  : 0.98
Release  : 4
URL      : http://pypi.debian.net/bz2file/bz2file-0.98.tar.gz
Source0  : http://pypi.debian.net/bz2file/bz2file-0.98.tar.gz
Source99 : https://pypi.python.org/packages/61/39/122222b5e85cd41c391b68a99ee296584b2a2d1d233e7ee32b4532384f2d/bz2file-0.98.tar.gz.asc
Summary  : Read and write bzip2-compressed files.
Group    : Development/Tools
License  : Apache-2.0
Requires: bz2file-python
BuildRequires : pbr
BuildRequires : pip
BuildRequires : python-dev
BuildRequires : python3-dev
BuildRequires : setuptools

%description
It contains a drop-in replacement for the file interface in the standard
        library's ``bz2`` module, including features from the latest development
        version of CPython that are not available in older releases.
        
        Bz2file is compatible with CPython 2.6, 2.7, and 3.0 through 3.4, as well as
        PyPy 2.0.
        
        
        Features
        --------
        
        - Supports multi-stream files.
        
        - Can read from or write to any file-like object.
        
        - Can open files in either text or binary mode.

%package python
Summary: python components for the bz2file package.
Group: Default

%description python
python components for the bz2file package.


%prep
%setup -q -n bz2file-0.98

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1503073052
python2 setup.py build -b py2
python3 setup.py build -b py3

%install
export SOURCE_DATE_EPOCH=1503073052
rm -rf %{buildroot}
python2 -tt setup.py build -b py2 install --root=%{buildroot} --force
python3 -tt setup.py build -b py3 install --root=%{buildroot} --force
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)
/usr/lib/python2*/*
/usr/lib/python3*/*
