# Based on https://gitlab.com/shadowblue/allthetools/-/blob/main/eza/eza.spec?ref_type=heads

%global debug_package %{nil}

Name: eza
# renovate: datasource=github-releases depName=eza-community/eza
Version: 0.21.5
Release: 1%{?dist}
Summary: A modern replacement for ls

License: EUPL-1.2
URL: https://github.com/eza-community/%{name}
Source: https://github.com/eza-community/%{name}/archive/refs/tags/v%{version}.tar.gz

BuildRequires: cargo
BuildRequires: rust
BuildRequires: pandoc

%description
eza is a modern, maintained replacement for the venerable file-listing
command-line program ls that ships with Unix and Linux operating systems,
giving it more features and better defaults.
It uses colours to distinguish file types and metadata.
It knows about symlinks, extended attributes, and Git.
And it’s small, fast, and just one single binary.

By deliberately making some decisions differently,
eza attempts to be a more featureful, more user-friendly version of ls.

%prep
%autosetup -n %{name}-%{version}

%build
cargo build --release --locked

%install
install -Dpm 0755 target/release/%{name} -t %{buildroot}%{_bindir}/
# Man
mkdir target/man
for page in eza.1 eza_colors.5 eza_colors-explanation.5; do
    sed "s/\$version/v%{version}/g" "man/${page}.md" | pandoc --standalone -f markdown -t man > "target/man/${page}"
done;
install -Dpm 0644 target/man/eza.1 -t %{buildroot}/%{_mandir}/man1/
install -Dpm 0644 target/man/eza_colors.5 -t %{buildroot}/%{_mandir}/man5/
install -Dpm 0644 target/man/eza_colors-explanation.5 -t %{buildroot}/%{_mandir}/man5/
# Shell completions
install -Dpm 0644 completions/bash/%{name} -t %{buildroot}/%{bash_completions_dir}
install -Dpm 0644 completions/fish/%{name}.fish -t %{buildroot}/%{fish_completions_dir}
install -Dpm 0644 completions/zsh/_%{name} -t %{buildroot}/%{zsh_completions_dir}

%check

%files
%license LICENSE.txt
%doc CHANGELOG.md README.md
%{_bindir}/%{name}
%{_mandir}/man1/eza.1*
%{_mandir}/man5/eza_colors*
%{bash_completions_dir}/%{name}
%{fish_completions_dir}/%{name}.fish
%{zsh_completions_dir}/_%{name}

%changelog
%autochangelog
