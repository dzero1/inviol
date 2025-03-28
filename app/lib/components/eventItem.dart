import 'package:app/models/event.dart';
import 'package:flutter/material.dart';

class EventItemView extends StatelessWidget {
  const EventItemView({super.key, required this.eventData});

  final Event eventData;

  @override
  Widget build(BuildContext context) {
    // Format date and time
    formatDateTime(DateTime dateTime) {
      // Convert to 12-hour format
      String hour = (dateTime.hour > 12 ? dateTime.hour - 12 : dateTime.hour)
          .toString()
          .padLeft(2, '0');

      // Add AM/PM
      String ampm = dateTime.hour > 12 ? "PM" : "AM";

      return "${dateTime.year}-${dateTime.month}-${dateTime.day} $hour:${dateTime.minute}:${dateTime.second} $ampm";
    }

    return ListTile(
      title: Text(eventData.description ?? "No description"),
      subtitle: Wrap(
        children: [
          const Text("Device ID: "),
          Text(eventData.device_id),
        ],
      ),
      trailing: Text(formatDateTime(eventData.timestamp)),
    );
  }
}
