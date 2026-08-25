#!/bin/bash
# Pubblica il portfolio MPLURE su GitHub Pages.
# Prerequisito una tantum:  gh auth login
set -e
cd "$(dirname "$0")"

REPO="mplure"
USER=$(gh api user --jq .login)

if ! gh repo view "$USER/$REPO" >/dev/null 2>&1; then
  echo "Creo il repository $USER/$REPO..."
  gh repo create "$REPO" --public --source=. --remote=origin --push
else
  git add -A
  git diff --staged --quiet || git commit -qm "aggiornamento portfolio $(date +%Y-%m-%d)"
  git push -q origin main
fi

# Attiva GitHub Pages sul branch main, cartella root
gh api -X POST "repos/$USER/$REPO/pages" \
  -f "source[branch]=main" -f "source[path]=/" 2>/dev/null \
  || gh api -X PUT "repos/$USER/$REPO/pages" \
       -f "source[branch]=main" -f "source[path]=/" 2>/dev/null || true

echo
echo "Portfolio online (attendi 1-2 minuti alla prima pubblicazione):"
echo "  italiano: https://$USER.github.io/$REPO/"
echo "  inglese:  https://$USER.github.io/$REPO/en/"
