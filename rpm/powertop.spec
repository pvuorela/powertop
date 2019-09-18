# 
# Do NOT Edit the Auto-generated Part!
# Generated by: spectacle version 0.27
# 

Name:       powertop

# >> macros
# << macros

Summary:    PowerTop is tool that is used for power diagnostics
Version:    2.7.1
Release:    1
Group:      Applications/System
License:    GPLv2
URL:        https://01.org/powertop/
Source0:    powertop-%{version}.tar.bz2
Source100:  powertop.yaml
Patch0:     0001-Disable-Qualcomm-mpdecision-binary-before-launching-.patch
Patch1:     0002-Baytrail-does-not-have-core-C7-MSR-to-read.patch
BuildRequires:  pkgconfig(ncursesw)
BuildRequires:  pkgconfig(libnl-3.0)
BuildRequires:  gettext
BuildRequires:  intltool

%description
PowerTop is tool that detects which Linux programs
and kernel tunables are resulting in the largest
power consumption and use of battery time. By
fixing (or closing) these applications or
processes, you can immediately see the power
savings in the tool. You'll also see the estimated
time left for battery power if you are running a
laptop.


%prep
%setup -q -n %{name}-%{version}/upstream

# 0001-Disable-Qualcomm-mpdecision-binary-before-launching-.patch
%patch0 -p1
%patch1 -p1
# >> setup
# << setup

%build
# >> build pre
%autogen
# << build pre

%configure --disable-static
make %{?_smp_mflags}

# >> build post
# << build post

%install
rm -rf %{buildroot}
# >> install pre
# << install pre
%make_install

# >> install post
mv %{buildroot}/usr/sbin/powertop %{buildroot}/usr/sbin/powertop-original
install -m 755 powertop.sh %{buildroot}/usr/sbin/powertop
# << install post

%find_lang powertop

%files -f powertop.lang
%defattr(-,root,root,-)
%doc COPYING
%doc /usr/share/man/man8/powertop.8.gz
%{_sbindir}/powertop-original
%{_sbindir}/powertop
# >> files
# << files
