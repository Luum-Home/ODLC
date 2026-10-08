#!/usr/bin/env bash
# verificar_fuentes_agentes.sh — chequea que las fuentes citadas en
# docs/08_referencias/Agentes abiertos y planes SaaS - Verificación.md
# sigan diciendo lo que la nota afirma.
#
# Read-only. Para cada fuente baja la página con curl y busca una frase
# literal. Además cuenta las CVEs de OpenClaw en NVD (la nota afirma "más
# de 500").
#
# Uso:   scripts/verificar_fuentes_agentes.sh
# Salida: una línea por fuente: OK / FALTA / ERROR.
# Exit:  0 todas OK · 1 alguna frase ya no está (la nota puede estar vencida)
#        2 error de red o HTTP (no se pudo verificar; no implica que esté mal)
#
# Fuentes que no responden a curl (help.openai.com da 403, el blog de
# Microsoft también) se listan al final como chequeo manual.

set -u

UA="Mozilla/5.0"
fallas=0
errores=0

chequear() {
  local url="$1" frase="$2" cuerpo codigo
  cuerpo=$(curl -sL --max-time 25 -A "$UA" -w $'\n%{http_code}' "$url") || {
    printf 'ERROR  curl falló       %s\n' "$url"; errores=$((errores + 1)); return; }
  codigo="${cuerpo##*$'\n'}"
  cuerpo="${cuerpo%$'\n'*}"
  if [ "$codigo" != "200" ]; then
    printf 'ERROR  HTTP %s           %s\n' "$codigo" "$url"; errores=$((errores + 1)); return
  fi
  if printf '%s' "$cuerpo" | grep -q -F -- "$frase"; then
    printf 'OK     %s\n' "$url"
  else
    printf 'FALTA  "%s"\n       en %s\n' "$frase" "$url"; fallas=$((fallas + 1))
  fi
}

NVD="https://services.nvd.nist.gov/rest/json/cves/2.0?cveId="

while IFS='|' read -r url frase; do
  [ -z "$url" ] && continue
  case "$url" in \#*) continue ;; esac
  chequear "$url" "$frase"
  # NVD sin API key acepta 5 pedidos cada 30 segundos.
  case "$url" in *services.nvd.nist.gov*) sleep 7 ;; esac
done <<'FUENTES'
# --- OpenClaw ---
https://raw.githubusercontent.com/openclaw/openclaw/main/LICENSE|Copyright (c) 2026 OpenClaw Foundation
https://services.nvd.nist.gov/rest/json/cves/2.0?cveId=CVE-2026-25253|before 2026.1.29 obtains a gatewayUrl value from a query string
https://services.nvd.nist.gov/rest/json/cves/2.0?cveId=CVE-2026-22172|OpenClaw versions prior to 2026.3.12 contain an authorization bypass
https://services.nvd.nist.gov/rest/json/cves/2.0?cveId=CVE-2026-32922|privilege escalation vulnerability in device.token.rotate
https://thehackernews.com/2026/02/researchers-find-341-malicious-clawhub.html|335 skills use fake pre-requisites
https://securityscorecard.com/blog/beyond-the-hype-moltbots-real-risk-is-exposed-infrastructure-not-ai-superintelligence/|40,214
https://docs.openclaw.ai/gateway/secrets|Plaintext still works. SecretRefs are opt-in per credential.
https://docs.openclaw.ai/gateway/security|container images default to an exposed bind
# --- Agent Zero ---
https://raw.githubusercontent.com/agent0ai/agent-zero/main/LICENSE|Copyright (c) 2025 Agent Zero, s.r.o
https://raw.githubusercontent.com/agent0ai/agent-zero/main/README.md|Review actions that touch accounts, money, production systems, or private data.
https://github.com/agent0ai/agent-zero/releases/tag/v1.9|CVE-2026-4308
https://services.nvd.nist.gov/rest/json/cves/2.0?cveId=CVE-2026-30624|remote code execution vulnerability in its External MCP Servers
https://services.nvd.nist.gov/rest/json/cves/2.0?cveId=CVE-2026-51852|agent-zero 1.7, 1.8, 1.9, and 1.10 is vulnerable to Directory Traversal
https://cheatsheetseries.owasp.org/cheatsheets/Docker_Security_Cheat_Sheet.html|equivalent to giving unrestricted root access to your host
# --- Hermes Agent ---
https://raw.githubusercontent.com/NousResearch/hermes-agent/main/LICENSE|Copyright (c) 2025 Nous Research
https://raw.githubusercontent.com/NousResearch/hermes-agent/main/README.md|Autonomous skill creation after complex tasks
https://hermes-agent.nousresearch.com/docs/user-guide/security|Use an auxiliary LLM to assess risk
https://cveawg.mitre.org/api/cve/CVE-2026-71963|RCE via git core.fsmonitor Config Injection
# --- Odysseus ---
https://raw.githubusercontent.com/odysseus-dev/odysseus/main/LICENSE|GNU AFFERO GENERAL PUBLIC LICENSE
https://raw.githubusercontent.com/odysseus-dev/odysseus/main/SECURITY.md|Security fixes are handled on the default branch until formal releases are cut
https://raw.githubusercontent.com/odysseus-dev/odysseus/main/SECURITY.md|shell, Python, file read/write, email send/read, MCP
# --- Claude ---
https://support.claude.com/en/articles/13345190-get-started-with-claude-cowork|Claude Cowork is available on paid plans
https://support.claude.com/en/articles/15036540-use-the-claude-agent-sdk-with-your-claude-plan|paused the previously-announced changes to Claude Agent SDK usage
https://support.claude.com/en/articles/15036540-use-the-claude-agent-sdk-with-your-claude-plan|Claude Max and Team plans now include
https://support.claude.com/en/articles/17154008-monthly-api-credits-for-max-and-team-plans|Free, Pro, and Enterprise plans aren't eligible
https://support.claude.com/en/articles/13837440|Plugins are available to all paid plans
https://support.claude.com/en/articles/12512180|Skills are available for users on Free, Pro, Max, Team, and Enterprise plans
https://code.claude.com/docs/en/sub-agents|~/.claude/agents/
# --- OpenAI (las de developers / learn sí responden a curl) ---
https://developers.openai.com/api/docs/guides/agent-builder|scheduled to shut down on
https://learn.chatgpt.com/docs/migrate-custom-gpts|transitioning custom GPTs to plugins
# --- Google ---
https://support.google.com/gemini/answer/15146780|Gems will go away on personal Google accounts
https://support.google.com/gemini/answer/17094507|Have a Google AI Pro or Ultra subscription
https://docs.cloud.google.com/gemini/enterprise/docs/editions|Build and publish custom no-code agents
# --- Agentes personales de los vendors ---
https://learn.chatgpt.com/docs/dots|Your dot is an always-on agent
https://learn.chatgpt.com/docs/dots|outside the European Economic Area, United Kingdom, and Switzerland
https://learn.chatgpt.com/docs/dots/controls|Ask for approval before taking the specified action
https://learn.chatgpt.com/docs/enterprise/dots-admin-guide|Enterprise model controls and defaults do not apply to dots
https://learn.chatgpt.com/docs/pricing|Plans at $100, $200, or $500 USD per month
https://docs.x.ai/grok-bot/overview.md|included with every paid individual Cursor plan
https://docs.x.ai/grok-bot/approvals-security-and-privacy.md|Do not use separate Bots as a security boundary.
https://docs.x.ai/grok-bot/security.md|Grok Bot computers run in the United States today.
https://docs.x.ai/grok-bot/security.md|Audit logs. Enterprise only.
https://cursor.com/help/grok-bot/plans|Grok Bot is not included
https://support.claude.com/en/articles/15520349-use-claude-cowork-on-web-desktop-and-mobile|new Cowork tasks on Pro and Max plans run in the cloud
https://support.claude.com/en/articles/13947068-assign-tasks-to-claude-from-anywhere-in-cowork|limited beta for Pro and Max plans
https://claude.com/docs/claude-tag/admins/setup-overview.md|available on individual plans
https://support.google.com/gemini/answer/17171264?hl=en|Google AI Pro subscribers in the US
https://about.fb.com/news/2026/09/introducing-muse-personal-ai-agent/|Muse is rolling out in the US on iOS, Android
FUENTES

# Conteo de CVEs de OpenClaw en NVD por CPE.
total=$(curl -s --max-time 30 -A "$UA" \
  "https://services.nvd.nist.gov/rest/json/cves/2.0?virtualMatchString=cpe:2.3:a:openclaw:openclaw&resultsPerPage=1" \
  | python3 -c 'import json,sys; print(json.load(sys.stdin)["totalResults"])' 2>/dev/null)
if [ -z "$total" ]; then
  printf 'ERROR  no se pudo contar CVEs de OpenClaw en NVD\n'; errores=$((errores + 1))
elif [ "$total" -ge 500 ]; then
  printf 'OK     NVD: %s CVEs de OpenClaw (la nota dice "más de 500")\n' "$total"
else
  printf 'FALTA  NVD: %s CVEs de OpenClaw (la nota dice "más de 500")\n' "$total"; fallas=$((fallas + 1))
fi

cat <<'MANUAL'

Chequeo manual (no responden a curl):
  help.openai.com/en/articles/8554407-gpts-in-chatgpt
      "New GPT creation and publishing are not available on personal ChatGPT accounts"
  help.openai.com/en/articles/20001519
      "Custom GPTs are scheduled to retire on Dec 11, 2026"
  help.openai.com/en/articles/11391654-chatgpt-business-release-notes
      "Workspace Agent runs now use token-based pricing"
  microsoft.com/en-us/security/blog/2026/02/19/running-openclaw-safely-identity-isolation-runtime-risk/
      "It is not appropriate to run on a standard personal or enterprise workstation."
MANUAL

printf '\nResumen: %d faltan, %d errores.\n' "$fallas" "$errores"
[ "$errores" -gt 0 ] && exit 2
[ "$fallas" -gt 0 ] && exit 1
exit 0
