Name: qm-dsp
Version: 1.7.1
Release: 1%{?dist}
Vendor:	The Centre for Digital Music
Summary: A C++ library for audio analysis
Group: Applications/Multimedia
License: GPL
URL: https://code.soundsoftware.ac.uk/projects/qm-dsp

Source: https://code.soundsoftware.ac.uk/attachments/download/1582/qm-dsp-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: gcc-c++


%description
This is a C++ library of functions for DSP and Music Informatics
purposes developed at Queen Mary, University of London.
It is used by the QM Vamp Plugins (q.v.) amongst other things.


%prep
%setup -q

%build
%ifarch %{ix86} x86_64
%{__make} -f build/linux/Makefile.linux64 %{?_smp_mflags}
%else
%{__make} -f build/linux/Makefile.linux32 %{?_smp_mflags}
%endif

%install
%{__rm} -rf %{buildroot}
install -D libqm-dsp.a %{buildroot}%{_libdir}/libqm-dsp.a

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc README.txt COPYING
%{_libdir}/libqm-dsp.a


%changelog
* Thu Sep 10 2015 Nicholas Humfrey
- Initial RPM spec creation for version 1.7.1
