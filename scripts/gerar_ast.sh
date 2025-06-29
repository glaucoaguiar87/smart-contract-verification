#!/bin/bash

for file in *.sol; do
  output="${file%.sol}.solast"
  echo "Gerando AST para: $file → $output"
  solc --ast-compact-json "$file" > "$output"

  # Corrigir problemas com campos null no .solast (evita erros no ESBMC)
  sed -i 's/"name": null/"name": ""/g' "$output"
done

echo "✅ Todos os arquivos .solast foram gerados com sucesso."
