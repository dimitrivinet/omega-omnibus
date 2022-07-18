import 'dart:html';

import 'package:flutter/material.dart';

Widget route(BuildContext context) {
  return Container(
    alignment: Alignment.center,
    color: const Color.fromARGB(255, 1, 4, 38),
    child: DefaultTextStyle(
        style: TextStyle(
            color: const Color.fromARGB(255, 254, 237, 159),
            decoration: TextDecoration.none,
            fontSize: DefaultTextStyle.of(context).style.fontSize),
        child: const HomeCenterText()),
  );
}

class HomeCenterText extends StatelessWidget {
  const HomeCenterText({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return Row(
      mainAxisAlignment: MainAxisAlignment.center,
      children: [
        Text("\u{03A9}",
            style:
                DefaultTextStyle.of(context).style.apply(fontSizeFactor: 3.0)),
        Column(
          mainAxisAlignment: MainAxisAlignment.center,
          crossAxisAlignment: CrossAxisAlignment.start,
          children: [Text("mega"), Text("mnibus")],
        )
      ],
    );
  }
}



// Text("Omega Omnibus",
//     style: TextStyle(
//         color: Color.fromARGB(255, 254, 237, 159),
//         decoration: TextDecoration.none));
