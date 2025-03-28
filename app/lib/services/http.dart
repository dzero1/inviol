import 'package:dio/dio.dart';
import 'package:flutter_dotenv/flutter_dotenv.dart';

final options = BaseOptions(
  baseUrl: dotenv.env['baseUrl']!,
  connectTimeout: const Duration(seconds: 10),
  receiveTimeout: const Duration(seconds: 30),
  headers: {
    'content-type': 'application/json',
  },
);

final dio = Dio(options);
