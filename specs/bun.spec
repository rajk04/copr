# Based on https://gitlab.com/mapanare-labs/packages/copr/bun/-/blob/main/bun.spec

%global debug_package %{nil}

Name: bun
# renovate: datasource=github-releases depName=oven-sh/bun
Version: 1.3.13
Release: 1%{?dist}
Summary: Bun is an all-in-one JavaScript runtime & toolkit designed for speed, complete with a bundler, test runner, and Node.js-compatible package manager.

License: MIT
URL: https://github.com/oven-sh/bun
Source: %{url}/releases/download/bun-v%{version}/bun-linux-aarch64.zip

%description
Bun is a new JavaScript runtime built from scratch to serve the modern JavaScript ecosystem. It has three major design goals:
- Speed. Bun starts fast and runs fast. It extends JavaScriptCore, the performance-minded JS engine built for Safari. Fast start times mean fast apps and fast APIs.
- Elegant APIs. Bun provides a minimal set of highly-optimized APIs for performing common tasks, like starting an HTTP server and writing files.
- Cohesive DX. Bun is a complete toolkit for building JavaScript apps, including a package manager, test runner, and bundler.

Bun is designed as a drop-in replacement for Node.js. It natively implements hundreds of Node.js and Web APIs, including fs, path, Buffer and more.

The goal of Bun is to run most of the world's server-side JavaScript and provide tools to improve performance, reduce complexity, and multiply developer productivity.

%prep
%autosetup -c

%build

%install
ls -Al
install -p -D %{name}-linux-aarch64/%{name} %{buildroot}%{_bindir}/%{name}

%check

%files
%{_bindir}/%{name}
