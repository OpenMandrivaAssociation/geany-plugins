%global geany_plug_docdir %{_defaultdocdir}/%{name}
Name:           geany-plugins
Version:        0.20
Release:        %mkrel 1

Group:          Development/GNOME and GTK+
License:        GPLv2+ ; GPLv3+
Summary:        A collection of different plugins for Geany
Url:            http://plugins.geany.org/
Source0:        http://plugins.geany.org/geany-plugins/geany-plugins-%{version}.tar.bz2
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:  gettext intltool pkgconfig
BuildRequires:  lua-devel enchant-devel gtkspell-devel
Requires:       geany >= 0.19
Requires:       lua

%description

Geany-Plugins is a collection of different plugins for Geany,
a lightweight IDE. It provides a common location for plugin authors
and users with a known infrastructure and support. List of included
plugins:


- Addons: Collection of small addons for geany
- Codenav: make it possible to
           - switch between header and implementation
           - go to a file by typing its name
- Geanydoc: allow executing specified commands on the
            current word at the cursor position
- Geanyextreasel: The Extra Selection adds several selection
                  enhancements to geany
- Geanygdb: integrated debugging support within Geany via
            the GNU Debugger (GDB).
- Geanyinsertnum: replaces a (possibly zero-width) rectangular selection
                  with integer numbers, using start/step/base etc.
                  specified by the user.
- Geanylatex: GeanyLaTeX is a plugin for Geany IDE to improve work
              with LaTeX.
- Geanylipsum: implements a Lorem Ipsum generator to insert
               placeholder text into your document
- Geanyprj: alternative project manager for Geany fast light IDE
- Geanysendmail: send a document as attachment using the preferred
                 mail client from inside Geany
- Geanyvc: provides a uniform way of accessing the different
           version-control systems inside Geany IDE.
- ShiftColumn: allows you to move blocks of text horizontally
- Spellcheck: checks the content of the current document in Geany
              with the spell check library Enchant
- Treebrowser

%prep
%setup -q

%build
%configure --docdir=%{geany_plug_docdir}
make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
make install -p DESTDIR=$RPM_BUILD_ROOT

# Remove static library *.la files
find $RPM_BUILD_ROOT -name '*.la' -exec rm -f '{}' \;

%find_lang %{name}


%clean
rm -rf $RPM_BUILD_ROOT


%files -f %{name}.lang
%defattr(-,root,root)
%doc NEWS README
%if "%{_libdir}" != "%{_libexecdir}"
%{_libexecdir}/geany-plugins
%endif
%{_libdir}/geany-plugins
%{_libdir}/geany/*
%{_datadir}/doc/geany-plugins
%{_datadir}/geany-plugins

