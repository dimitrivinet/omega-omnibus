import 'package:flutter/material.dart';
import 'routes/home.dart' as home;

Map<String, WidgetBuilder> getRoutes() {
  return {
    // '/': (BuildContext context) => root.route(context),
    '/home': (BuildContext context) => home.route(context),
  };
}
