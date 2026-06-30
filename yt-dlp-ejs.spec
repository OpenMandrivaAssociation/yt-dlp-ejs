Name:           yt-dlp-ejs
# Keep in sync with https://github.com/yt-dlp/yt-dlp/blob/2025.11.12/pyproject.toml#L59
Version:        0.8.0
Release:        1
Summary:        External JavaScript for yt-dlp supporting many runtimes

License:        Unlicense license, MIT AND ISC
URL:            https://github.com/yt-dlp/ejs
# Remember to also update source1 and source2 each time
Source0:	https://github.com/yt-dlp/ejs/releases/download/%{version}/yt_dlp_ejs-%{version}.tar.gz
# mirror https://files.pythonhosted.org/packages/source/y/yt_dlp_ejs/yt_dlp_ejs-%{version}.tar.gz
Source1:        https://github.com/yt-dlp/ejs/releases/download/%{version}/yt.solver.core.min.js
Source2:        https://github.com/yt-dlp/ejs/releases/download/%{version}/yt.solver.lib.min.js

BuildArch:      noarch
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(hatch-vcs)
BuildRequires:  python3dist(hatchling)
BuildRequires:  (quickjs or quikcjs-ng or deno or bun or nodejs)
# Recommended is deno but is rust based and currently not packaged for OMV, so lets pick at first quickjs
Requires:  (quickjs or quickjs-ng or deno or bun or nodejs)

%description
External JavaScript for yt-dlp supporting many runtimes

%prep
%autosetup -p1 -n yt_dlp_ejs-%{version}

# extract additional files
cp %{SOURCE1} yt_dlp_ejs/yt/solver/core.min.js
cp %{SOURCE2} yt_dlp_ejs/yt/solver/lib.min.js

%build
%py_build

%install
%py_install

%files
