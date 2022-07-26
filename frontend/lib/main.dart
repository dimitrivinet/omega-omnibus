// Copyright 2018 The Flutter team. All rights reserved.
// Use of this source code is governed by a BSD-style license that can be
// found in the LICENSE file.

import 'package:flutter/foundation.dart';
import 'package:flutter/material.dart';
import 'package:frontend/src/game/cards/cards.dart';
import 'package:frontend/src/routes/root.dart';
import 'package:frontend/src/theme.dart' as theme;

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
      theme: theme.OOTheme.theme,
      // home: const RootPage(),
      home: const Cards(),
    );
    // home: home.route(context),
  }
}
