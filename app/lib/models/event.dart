import 'dart:convert';

import 'package:app/services/http.dart';

class Event {
  int? id;
  String device_id = "";
  DateTime timestamp = DateTime.now();
  String? description;
  Map? meta;

  // Constructor
  Event(
      {this.id,
      required this.device_id,
      required this.timestamp,
      this.description,
      this.meta});

  // Convert a Map to an Event
  factory Event.fromJson(Map<String, dynamic> json) => Event(
        id: json['id'],
        device_id: json['device_id'],
        timestamp: DateTime.parse(json['timestamp']),
        description: json['description'],
        meta: json['meta'],
      );

  @override
  toString() => json.encode({
        "device_id": device_id,
        "timestamp": timestamp.toString(),
        "description": description,
        "meta": meta
      });

  save() async {
    String data = toString();
    final response = await dio.post('/events', data: {
      "device_id": device_id,
      "timestamp": timestamp.toString(),
      "description": description,
      "meta": meta
    });

    return response.statusCode == 200;
  }
}
