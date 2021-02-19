#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xF5AA16828D5E4230 (nadeem.vawda@gmail.com)
#
Name     : bz2file
Version  : 0.98
Release  : 33
URL      : http://pypi.debian.net/bz2file/bz2file-0.98.tar.gz
Source0  : http://pypi.debian.net/bz2file/bz2file-0.98.tar.gz
Source1  : http://pypi.debian.net/bz2file/bz2file-0.98.tar.gz.asc
Summary  : Read and write bzip2-compressed files.
Group    : Development/Tools
License  : Apache-2.0
Requires: bz2file-python = %{version}-%{release}
Requires: bz2file-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3

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
Requires: bz2file-python3 = %{version}-%{release}

%description python
python components for the bz2file package.


%package python3
Summary: python3 components for the bz2file package.
Group: Default
Requires: python3-core
Provides: pypi(bz2file)

%description python3
python3 components for the bz2file package.


%prep
%setup -q -n bz2file-0.98
cd %{_builddir}/bz2file-0.98

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1603388399
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
