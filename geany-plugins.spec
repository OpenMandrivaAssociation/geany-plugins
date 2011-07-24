%define use_ccache		1
%define ccachedir		~/.ccache-OOo%{mdvsuffix}%{?_with_ccache: %global use_ccache 1}%{?_without_ccache: %global use_ccache 0}
%define enable_debug_packages	%{nil}
%define debug_package		%{nil}

%define version			0.20
%define release			1

%global geany_plug_docdir 	%{_defaultdocdir}/%{name}-%{version}
%global req_geany_ver		0.20

Name:           geany-plugins
Version:        %{version}
Release:        %mkrel %{release}
Summary:        Plugins for Geany
Group:          Development/Other
License:        GPLv2+
URL:            http://plugins.geany.org/
Source0:        http://plugins.geany.org/geany-plugins/geany-plugins-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires:	geany >= %{req_geany_ver}
BuildRequires:	gettext
BuildRequires:	pkgconfig
BuildRequires:	intltool
BuildRequires:  lua-devel
BuildRequires:	enchant-devel
BuildRequires:	gtkspell-devel
BuildRequires:	ctpl
Obsoletes:      geanygdb

%description
Plugins for Geany. Plugins included are:
* Addons (various small addons)
* Codenav (Navigating in Geany)
* GeanyExtrasel
* Geanygdb (provides integration with gdb)
* GeanyGenDoc
* GeanyInsertNum
* Geanylatex (improved support for LaTeX documents)
* Geanylipsum (for inserting blocks of Lorem Ipsum text)
* Geanylua (provides support for scripting with Lua)
* Geanysendmail (allows sending of documents from within Geany)
* Geanyvc (support for various version control systems)
* Pretty Printer
* Shiftcolumn (for moving blocks of text horizontally)
* Spellcheck (for spell checking documents)
* TreeBrowser
* UpdateChecker
* WebHelper

%package common
Summary:   Common files used by all geany plugins
Group:     Development/Tools
Requires:  geany >= %{req_geany_ver}

%description common
This package contains some common files which are used by every Geany plugin,
e.g. language translations.

%package addons
Summary:   Miscellaneous Addons for Geany
Group:     Development/Tools
Requires:  geany >= %{req_geany_ver}
Requires:  geany-plugins-common = %{version}-%{release}

%description addons
This plugins consists of various small addons too small to justify their own
plugin, but are useful to have. The following functionality is implemented:
* Doclist: This addon places a new item in the toolbar and when clicked offers
  a menu listing all open files plus the 'Close All' and 'Close Other
  Documents' menu items. This can be useful to quickly access open files and
  switch to them.
* OpenURI: Adds 'Open URI' and 'Copy URI' menu items to the editor menu when
  the word under the cursor looks like a URI. 'Open URI' uses the browser
  command configured in Geany to open it.
* Tasks:The tasks plugin goes through a file being edited and picks out lines
  with "TODO" or "FIXME" in them. It collects the text after those words and
  puts them in a new "Tasks" tab in the message window. Clicking on a task in
  that tab takes you to the line in the file where the task was defined.
* Systray: Adds a status icon to the notification area (systray) and provides
  a simple popup menu with some basic actions. It can also be used to quickly
  show and hide the Geany main window.

%package codenav
Summary:   Navigating in the code for Geany
Group:     Development/Tools
Requires:  geany >= %{req_geany_ver}
Requires:  geany-plugins-common = %{version}-%{release}

%description codenav
This plugin adds some facilities for navigating in the code.
Actually, it will make it possible to :
- switch between header and implementation
- go to a file by typing its name

%package geanydoc
Summary:   Search documentation for Geany
Group:     Development/Tools
Requires:  geany >= %{req_geany_ver}
Requires:  geany-plugins-common = %{version}-%{release}

%description geanydoc
Geanydoc is plugin for Geany IDE that allow execute specified commands on the
current word at the cursor position. This word is passed as an argument to these commands.
It allow either place output of these commands in geany buffer \*DOC\* or just
execute external program. Geanydoc is intended to be used for searching documentation
API in different sources.

%package geanyextrasel
Summary:   Extra selection for Geany
Group:     Development/Tools
Requires:  geany >= %{req_geany_ver}
Requires:  geany-plugins-common = %{version}-%{release}

%description geanyextrasel
The Extra Selection adds the following functions:

Goto matching brace and select (Select to matching brace).

Goto line and select (Select to line).

Ctrl-Shift-Alt-Left/Right/Home/End keys - same as Ctrl-Shift, but for
rectangular selection.

Column mode - while active, all (Ctrl)-Shift-movement keys do rectangle
selection instead of stream.

"Movement keys" refers to the arrows, Home, End, Page Up and Page Down.

%package geanygdb
Summary:   Debugger Plugin for Geany using GDB
Group:     Development/Tools
Requires:  geany >= %{req_geany_ver}
Requires:  geany-plugins-common = %{version}-%{release}
Requires:  gdb
Obsoletes: geanygdb

%description geanygdb
GeanyGDB plugin provides an integrated debugging environment for the
GNU debugger (gdb).

%package geanygendoc
Summary:   Generate documentation for Geany
Group:     Development/Tools
Requires:  geany >= %{req_geany_ver}
Requires:  geany-plugins-common = %{version}-%{release}
Requires:  ctpl

%description geanygendoc
A plugin for Geany that aims to automatically
generate documentation comment basis from the source code.

%package geanyinsertnum
Summary:   Insert number for Geany
Group:     Development/Tools
Requires:  geany >= %{req_geany_ver}
Requires:  geany-plugins-common = %{version}-%{release}

%description geanyinsertnum
This plugin replaces a (possibly zero-width) rectangular selection with
integer numbers, using start/step/base etc. specified by the user.
For practical reasons, the number of lines is limited to 500000.

%package geanylatex
Summary:   LaTeX support for Geany
Group:     Development/Tools
Requires:  geany >= %{req_geany_ver}
Requires:  geany-plugins-common = %{version}-%{release}
Requires:  tetex, tetex-dvips, tetex-latex, fonts-ttf-latex


%description geanylatex
This plugin improves LaTeX support in Geany. It provides several templates for
new documents, help with adding labels and inserting special characters,
and much more.

%package geanyprj
Summary:   Alternative project manager for Geany fast light IDE
Group:     Development/Tools
Requires:  geany >= %{req_geany_ver}
Requires:  geany-plugins-common = %{version}-%{release}

%description geanyprj
Geanyprj is alternative project manager for Geany fast light IDE.
Open source is great, there are a lot of nice sources that you can use for your projects
in Internet. But there are also a lot of crappy sources and when you want steal something
you need to check if it is good or not. Ability to jump to definition/declaration and back is
great help for such task. But no other text editor or IDE I know allow this without a lot of setuping.
You have to create/import project add files. When you finish with one project
you need to close it and repeat procedure for all other. Great time wasting. If you are checking
about 10 potential places you want steal code from, you won't create any project and don't
get "jump to definition/declaration" just because it is too much bother.

geanyprj aims to provide "jump to definition/declaration" functions with as little setup as possible.


%package geanylipsum
Summary:   Lorem Ipsum generator for Inserting Placeholder Text
Group:     Development/Tools
Requires:  geany >= %{req_geany_ver}
Requires:  geany-plugins-common = %{version}-%{release}

%description geanylipsum
GeanyLipsum is a Lorem Ipsum generator for inserting placeholder text into a
document.

%package geanylua
Summary:   Lua Scripting for Geany
Group:     Development/Tools
Requires:  geany >= %{req_geany_ver}
Requires:  geany-plugins-common = %{version}-%{release}
Requires:  lua

%description geanylua
This plugin provides extensive support for developing in the lua programming
language.

%package geanysendmail
Summary:   Send E-Mails from within Geany
Group:     Development/Tools
Requires:  geany >= %{req_geany_ver}
Requires:  geany-plugins-common = %{version}-%{release}

%description geanysendmail
GeanySendMail is a little plugin to send a document as attachment using the
preferred mail client from inside Geany. It is similar to the envelope symbol
of most office tools and requires a mail client that supports remote calls.

%package geanyvc
Summary:   Version Control for Geany
Group:     Development/Tools
Requires:  geany >= %{req_geany_ver}
Requires:  geany-plugins-common = %{version}-%{release}
Obsoletes: geanyvc <= 0.5
Provides:  geanyvc = %{version}-%{release}

%description geanyvc
Geanyvc is a plugin that provides a uniform way of accessing different version
control systems from within the Geany IDE. Currently, support for the following
version control systems is provided:

* Bazaar
* Git
* Mercurial
* Subversion
* SVK
* CVS

%package prettyprinter
Summary:   Pretty printer for Geany
Group:     Development/Tools
Requires:  geany >= %{req_geany_ver}
Requires:  geany-plugins-common = %{version}-%{release}

%description prettyprinter
Another pretty way to printing in Geany.

%package shiftcolumn
Summary:   Move Blocks of Text horizontally
Group:     Development/Tools
Requires:  geany >= %{req_geany_ver}
Requires:  geany-plugins-common = %{version}-%{release}

%description shiftcolumn
Shiftcolumn allows you to move blocks of text horizontally in Geany.

%package spellcheck
Summary:   Spellcheck Text in Geany using the Enchant Library
Group:     Development/Tools
Requires:  geany >= %{req_geany_ver}
Requires:  geany-plugins-common = %{version}-%{release}
Requires:  enchant

%description spellcheck
Spellcheck checks the selected text (or the whole document) with the spellcheck
library Enchant

%package treebrowser
Summary:   Treebrowser plug-in for Geany
Group:     Development/Tools
Requires:  geany >= %{req_geany_ver}
Requires:  geany-plugins-common = %{version}-%{release}

%description treebrowser
You can view your projects in treebrowser view in Geany.

%package updatechecker
Summary: 	UpdateChecker plug-in for Geany
Group:		Development/Tools
Requires:	geany >= %{req_geany_ver}
Requires:	geany-plugins-common = %{version}-%{release}

%description updatechecker
UpdateChecker is a plugin for Geany, which is able to check whether
there is a more recent version of Geany available.

%package webhelper
Summary: 	WebHelper plug-in for Geany
Group:		Development/Tools
Requires:	geany >= %{req_geany_ver}
Requires:	geany-plugins-common = %{version}-%{release}

%description webhelper
WebHelper is a plugin for Geany that provides some web development facilities,
such as a web page preview and some debugging tools (web inspector).

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

%files common -f %{name}.lang
%defattr(-,root,root,-)
%dir %{_libdir}/%{name}/
%dir %{_datadir}/%{name}/

%files addons
%defattr(-,root,root,-)
%doc %{geany_plug_docdir}/addons
%{_libdir}/geany/addons.*

%files codenav
%defattr(-,root,root,-)
%doc %{geany_plug_docdir}/codenav
%{_libdir}/geany/codenav.*

%files geanydoc
%defattr(-,root,root,-)
%doc %{geany_plug_docdir}/geanydoc
%{_libdir}/geany/geanydoc.*

%files geanyextrasel
%defattr(-,root,root,-)
%doc %{geany_plug_docdir}/geanyextrasel
%{_libdir}/geany/geanyextrasel.*

%files geanygdb
%defattr(-,root,root,-)
%doc %{geany_plug_docdir}/geanygdb/
%{_libdir}/geany/geanygdb.*
%{_libexecdir}/geany-plugins/geanygdb/ttyhelper

%files geanygendoc
%defattr(-,root,root,-)
%doc %{geany_plug_docdir}/geanygendoc/
%{_datadir}/geany-plugins/geanygendoc/
%{_libdir}/geany/geanygendoc.*

%files geanyinsertnum
%defattr(-,root,root,-)
%doc %{geany_plug_docdir}/geanyinsertnum/
%{_libdir}/geany/geanyinsertnum.*

%files geanylatex
%defattr(-,root,root,-)
%doc %{geany_plug_docdir}/geanylatex/
%{_libdir}/geany/geanylatex.*

%files geanylipsum
%defattr(-,root,root,-)
%doc %{geany_plug_docdir}/geanylipsum/
%{_libdir}/geany/geanylipsum.so

%files geanylua
%defattr(-,root,root,-)
%doc %{geany_plug_docdir}/geanylua/
%{_libdir}/geany/geanylua.*
%{_datadir}/%{name}/geanylua/
%{_libdir}/%{name}/geanylua/

%files geanyprj
%defattr(-,root,root,-)
%doc %{geany_plug_docdir}/geanyprj/
%{_libdir}/geany/geanyprj.*


%files geanysendmail
%defattr(-,root,root,-)
%doc %{geany_plug_docdir}/geanysendmail/
%{_libdir}/geany/geanysendmail.*

%files geanyvc
%defattr(-,root,root,-)
%doc %{geany_plug_docdir}/geanyvc/
%{_libdir}/geany/geanyvc.*

%files prettyprinter
%defattr(-,root,root,-)
%{_libdir}/geany/pretty-print.*

%files shiftcolumn
%defattr(-,root,root,-)
%doc %{geany_plug_docdir}/shiftcolumn/
%{_libdir}/geany/shiftcolumn.*

%files spellcheck
%defattr(-,root,root,-)
%doc %{geany_plug_docdir}/spellcheck/
%{_libdir}/geany/spellcheck.*

%files treebrowser
%defattr(-,root,root,-)
%doc %{geany_plug_docdir}/treebrowser/
%{_libdir}/geany/treebrowser.*

%files updatechecker
%defattr(-,root,root,-)
%doc %{geany_plug_docdir}/updatechecker/
%{_libdir}/geany/updatechecker.*

%files webhelper
%defattr(-,root,root,-)
%doc %{geany_plug_docdir}/webhelper/
%{_libdir}/geany/webhelper.*