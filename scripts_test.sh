#!/usr/bin/env bash

set -e

BASE_URL="http://localhost:8000"

echo "== Healthcheck =="
curl -s "$BASE_URL/health"
echo
echo

echo "== Crear usuario demo =="
curl -s -X POST "$BASE_URL/users/" \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Usuario Demo",
    "email": "demo@example.com",
    "age": 28
  }'
echo
echo

echo "== Listar usuarios =="
curl -s "$BASE_URL/users/"
echo
echo

echo "== Obtener usuario 1 =="
curl -s "$BASE_URL/users/1"
echo
echo

echo "== Actualizar usuario 1 =="
curl -s -X PUT "$BASE_URL/users/1" \
  -H "Content-Type: application/json" \
  -d '{"age": 29}'
echo
echo

echo "== Listar usuarios actualizado =="
curl -s "$BASE_URL/users/"
echo
