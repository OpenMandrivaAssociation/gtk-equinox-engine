%define tarname	equinox-gtk-engine
%define name	gtk-equinox-engine
%define version	1.20
%define release %mkrel 1

%define libname %mklibname %{name}

%define gtkbinaryver %(if $([ -x %{_bindir}/pkg-config ] && pkg-config --exists gtk+-2.0); then pkg-config --variable=gtk_binary_version gtk+-2.0; else echo 0; fi)

Summary:	Equinox engine for Gtk 2.x
Name:		%{name}
Version:	%{version}
Release:	%{release}
Source0:	%{tarname}.tar.gz
Source1:	equinox-themes.tar.gz
License:	GPLv2+
Group:		Graphical desktop/Other
Url:		http://www.gnome-look.org
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
Requires:	%{libname} = %{version}
BuildRequires:	gtk2-devel >= 2.12

%description
A heavily modified version of the beautiful Aurora engine.

%package -n %{libname}
Summary:    Library files for %{name}
Group:	    System/Libraries
Provides:   %{libname} = %{version}
Requires:   gtk+2.0

%description -n %{libname}
Library files for %{name}.

%prep
%setup -q -n equinox-%{version}

%build
%configure2_5x --enable-animation
%make

%install
%__rm -rf %{buildroot}
%makeinstall
%__mkdir -p %{buildroot}%{_datadir}/themes
%__tar zfx %SOURCE1 -C %{buildroot}%{_datadir}/themes

# Fix bug 56215:
#sed -i 's/\(^.*odd_row_color.*\)/\#\1/' %{buildroot}%{_datadir}/themes/Aurora*/gtk-2.0/gtkrc

%clean
%__rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README COPYING ChangeLog AUTHORS
%{_datadir}/themes/*

%files -n %{libname}
%defattr(-,root,root)
%{_libdir}/gtk-2.0/%{gtkbinaryver}/engines/*.*
