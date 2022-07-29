// Copyright 2018 The Flutter team. All rights reserved.
// Use of this source code is governed by a BSD-style license that can be
// found in the LICENSE file.

import 'package:flutter/foundation.dart';
import 'package:flutter/material.dart';
import 'package:frontend/src/components/info_page.dart';
import 'package:frontend/src/game/cards/cards.dart';
import 'package:frontend/src/routes/root.dart';
import 'package:frontend/src/theme.dart' as theme;

import "src/pages/home.dart" as home;
import "src/pages/about.dart" as about;
import "src/pages/contact.dart" as contact;

void main() {
  runApp(const MyApp());
}

class MyApp extends StatefulWidget {
  const MyApp({Key? key}) : super(key: key);

  @override
  // ignore: library_private_types_in_public_api
  _MyAppState createState() => _MyAppState();
}

class _MyAppState extends State<MyApp> {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      routes: {
        "/": (context) => const home.OOHome(),
        "/new_game": (context) => OOInfoPage("New Game", child: Container()),
        "/history": (context) => OOInfoPage("History", child: Container()),
        "/stats": (context) => OOInfoPage("Stats", child: Container()),
        "/about": (context) => const about.OOAbout(),
        "/contact": (context) => const contact.OOContact(),
      },
    );
    // home: home.route(context),
  }
}
