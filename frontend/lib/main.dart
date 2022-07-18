// Copyright 2018 The Flutter team. All rights reserved.
// Use of this source code is governed by a BSD-style license that can be
// found in the LICENSE file.

import 'package:flutter/material.dart';
import 'src/router.dart' as router;
import 'package:google_fonts/google_fonts.dart';

void main() {
  runApp(const MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
        routes: router.getRoutes(),
        theme: ThemeData(
            primarySwatch: Colors.amber,
            textTheme: GoogleFonts.solwayTextTheme(
              Theme.of(context).textTheme,
            )));
  }
}
