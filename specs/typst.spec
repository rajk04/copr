# Based on https://github.com/simonhammes/copr/blob/main/specs/typst.spec

%global debug_package %{nil}

Name: typst
# renovate: datasource=github-releases depName=typst/typst
Version: 0.13.1
Release: 3%{?dist}
Summary: A new markup-based typesetting system that is powerful and easy to learn

License: Apache-2.0
URL: https://github.com/typst/typst
Source: %{url}/releases/download/v%{version}/%{name}-%{arch}-unknown-linux-musl.tar.xz

%description
Typst is a new markup-based typesetting system that is designed to be as powerful as LaTeX while being much easier to learn and use.
Typst has:

- Built-in markup for the most common formatting tasks
- Flexible functions for everything else
- A tightly integrated scripting system
- Math typesetting, bibliography management, and more
- Fast compile times thanks to incremental compilation
- Friendly error messages in case something goes wrong

%prep
%autosetup -c

%build

%install
ls -Al
install -p -D %{name}-%{arch}-unknown-linux-musl/%{name} %{buildroot}%{_bindir}/%{name}

%check

%files
%{_bindir}/%{name}