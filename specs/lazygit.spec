# Based on https://github.com/RelativeSure/autocopr/blob/main/specs/lazygit.spec

%global debug_package %{nil}

Name:    lazygit
# renovate: datasource=github-releases depName=jesseduffield/lazygit
Version: 0.58.1
Release: 1%{?dist}
Summary: simple terminal UI for git commands

License: MIT
URL: https://github.com/jesseduffield/lazygit
Source: %{url}/releases/download/v%{version}/%{name}_%{version}_Linux_arm64.tar.gz
Source1: https://raw.githubusercontent.com/jesseduffield/lazygit/v%{version}/README.md
Source2: https://raw.githubusercontent.com/jesseduffield/lazygit/v%{version}/LICENSE

%description
%{summary}

%prep
%autosetup -c
cp %{SOURCE1} CONFIGURATION.md
cp %{SOURCE2} LICENSE

%build

%install
install -p -D %{name} %{buildroot}%{_bindir}/%{name}

%check

%files
%doc CONFIGURATION.md
%license LICENSE
%{_bindir}/%{name}

%changelog
%autochangelog