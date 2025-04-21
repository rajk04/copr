# Based on https://gitlab.com/shadowblue/allthetools/-/blob/main/starship/starship.spec

%global debug_package %{nil}

Name:    starship
# renovate: datasource=github-releases depName=starship/starship
Version: 1.22.1
Release: 2%{?dist}
Summary: The minimal, blazing-fast, and infinitely customizable prompt for any shell!
License: ISC
URL: https://github.com/starship/%{name}
Source: https://github.com/starship/%{name}/archive/refs/tags/v%{version}.tar.gz
BuildRequires: cmake
BuildRequires: cargo
BuildRequires: rust

%description
The minimal, blazing-fast, and infinitely customizable prompt for any shell!
- Fast: it's fast – really really fast! 🚀
- Customizable: configure every aspect of your prompt.
- Universal: works on any shell, on any operating system.
- Intelligent: shows relevant information at a glance.
- Feature rich: support for all your favorite tools.
- Easy: quick to install – start using it in minutes.

%prep
%autosetup -n %{name}-%{version}

%build
cargo build --release --locked

%install
install -Dpm 0755 target/release/%{name} -t %{buildroot}%{_bindir}/

%check

%files
%license LICENSE
%doc CHANGELOG.md README.md
%{_bindir}/%{name}

%changelog
%autochangelog
