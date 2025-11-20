Name:           yt-dlp-ejs
# Keep in sync with https://github.com/yt-dlp/yt-dlp/blob/2025.11.12/pyproject.toml#L59
Version:        0.3.1
Release:        1
Summary:        External JavaScript for yt-dlp supporting many runtimes

License:        Unlicense license, MIT AND ISC
URL:            https://github.com/yt-dlp/ejs
Source0:        https://files.pythonhosted.org/packages/source/y/yt_dlp_ejs/yt_dlp_ejs-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(hatch-vcs)
BuildRequires:  python3dist(hatchling)
# Recommended is deno but is rust based and currently not packaged for OMV, so lets pick at first quickjs
Requires:  (quickjs or deno or bun or nodejs)
BuildSystem:	python

%description
External JavaScript for yt-dlp supporting many runtimes

%prep
%autosetup -p1 -n yt_dlp_ejs-%{version}

%files
