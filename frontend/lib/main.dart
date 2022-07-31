// Copyright 2018 The Flutter team. All rights reserved.
// Use of this source code is governed by a BSD-style license that can be
// found in the LICENSE file.

import 'package:flutter/material.dart';

import "package:frontend/src/pages/about.dart" as about;
import "package:frontend/src/pages/contact.dart" as contact;
import "package:frontend/src/pages/game/history.dart" as history;
import "package:frontend/src/pages/game/new_game.dart" as new_game;
import "package:frontend/src/pages/game/stats.dart" as stats;
import "package:frontend/src/pages/home.dart" as home;

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
        "/new_game": (context) => const new_game.OONewGame(),
        "/history": (context) => const history.OOHistory(),
        "/stats": (context) => const stats.OOStats(),
        "/about": (context) => const about.OOAbout(),
        "/contact": (context) => const contact.OOContact(),
      },
    );
    // home: home.route(context),
  }
}
