%global geany_plug_docdir %{_defaultdocdir}/%{name}
%define _disable_rebuild_configure 1

Summary:	A collection of different plugins for Geany
Name:		geany-plugins
Version:	2.0
Release:	1
License:	GPLv2+ and GPLv3+
Group:		Development/GNOME and GTK+
Url:		http://plugins.geany.org/
Source0:	http://plugins.geany.org/geany-plugins/%{name}-%{version}.tar.bz2
BuildRequires:	gettext
BuildRequires:	intltool
BuildRequires:	pkgconfig(enchant)
BuildRequires:	pkgconfig(geany)
BuildRequires:	pkgconfig(gtkspell-2.0)
BuildRequires:	pkgconfig(lua) < 5.2
BuildRequires:	pkgconfig(python)
BuildRequires:        pkgconfig(gtk+-3.0)
Requires:	geany
Requires:	lua5.1

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

%files -f %{name}.lang
%doc %{_datadir}/doc/geany-plugins/
%{_libdir}/geany-plugins
%{_libdir}/geany/*
%{_libdir}/libgeanypluginutils.so*
%{_datadir}/geany-plugins

#----------------------------------------------------------------------------

%prep
%autosetup -p1

%build
%configure --docdir=%{geany_plug_docdir}
%make_build

%install
%make_install

%find_lang %{name}
