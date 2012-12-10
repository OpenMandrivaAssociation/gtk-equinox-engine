%define tarname	equinox-gtk-engine
%define name	gtk-equinox-engine
%define version	1.50
%define release 1

%define libname %mklibname %{name}

%define gtkbinaryver %(if $([ -x %{_bindir}/pkg-config ] && pkg-config --exists gtk+-2.0); then pkg-config --variable=gtk_binary_version gtk+-2.0; else echo 0; fi)

Summary:	Equinox engine for Gtk 2.x
Name:		%{name}
Version:	%{version}
Release:	%{release}
Source0:	%{tarname}.tar.gz
Source1:	equinox-themes.tar.gz
patch1:		equinox-gtk-engine-1.50.glibh.patch
License:	GPLv2+
Group:		Graphical desktop/Other
Url:		http://www.gnome-look.org
Requires:	%{libname} = %{version}
BuildRequires:	pkgconfig(gtk+-2.0) >= 2.12

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
%setup -q -n equinox-1.50
%apply_patches
chmod u-x src/*

%build
%configure2_5x --enable-animation
%make

%install
%makeinstall
%__mkdir -p %{buildroot}%{_datadir}/themes
%__tar zfx %SOURCE1 -C %{buildroot}%{_datadir}/themes

# Fix bug 56215:
#sed -i 's/\(^.*odd_row_color.*\)/\#\1/' %{buildroot}%{_datadir}/themes/Aurora*/gtk-2.0/gtkrc

%files
%defattr(644,root,root,755)
%doc README COPYING ChangeLog AUTHORS
%{_datadir}/themes/*

%files -n %{libname}
%defattr(755,root,root,755)
%{_libdir}/gtk-2.0/%{gtkbinaryver}/engines/*.*


%changelog
* Sun May 01 2011 Lev Givon <lev@mandriva.org> 1.50-1mdv2011.0
+ Revision: 661355
- Update to 1.50.

* Wed Oct 06 2010 Lev Givon <lev@mandriva.org> 1.30.2-1mdv2011.0
+ Revision: 583877
- Update to 1.30.2.

* Tue Sep 07 2010 Lev Givon <lev@mandriva.org> 1.30-1mdv2011.0
+ Revision: 576669
- Update to 1.30.

* Sun Aug 01 2010 Lev Givon <lev@mandriva.org> 1.20-1mdv2011.0
+ Revision: 564886
- import gtk-equinox-engine


