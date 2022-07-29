import 'package:flutter/material.dart';

class OOBackButton extends StatelessWidget {
  final Color color;
  final Color backgroundColor;

  const OOBackButton(this.color, this.backgroundColor, {Key? key})
      : super(key: key);

  @override
  Widget build(BuildContext context) {
    return Material(
      color: backgroundColor,
      child: IconButton(
        icon: const Icon(Icons.arrow_back),
        color: color,
        onPressed: () => Navigator.pop(context),
      ),
    );
  }
}
