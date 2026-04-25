# SECURITY-AND-ACCESS.md
## Política de seguridad y acceso — Sistema /RAUL/

**Versión:** 1.0
**Última actualización:** 2026-04-25

---

## 1. Datos sensibles — qué NO va en el repo

Los siguientes elementos **nunca** deben escribirse en archivos del repo ni en prompts a LLMs:

- Contraseñas, PINs, claves de acceso.
- Tokens de API (Google, Anthropic, OpenAI, GitHub, etc.).
- Datos personales identificables de terceros (nombre completo + contacto + información médica/financiera juntos).
- Números de cuenta bancaria, tarjetas, datos fiscales.
- Información confidencial de clientes o contratos bajo NDA.

Si una tarea requiere manejar datos de este tipo, procesarlos localmente en memoria o en archivos fuera del repo, nunca persistirlos en `/RAUL/`.

---

## 2. Credenciales y tokens

- Los tokens de API viven en variables de entorno o gestores de credenciales del sistema operativo, nunca en `.md` ni `.py` del repo.
- El `.gitignore` excluye `*.env` y archivos de credenciales por defecto.
- Si un script necesita credenciales, debe leerlas desde variables de entorno (`os.environ`) o solicitar al Owner que las provea en la sesión.

---

## 3. Acceso al repo GitHub

- Repo: `https://github.com/raoulbermudez-jpg/RAUL.git`
- Rama principal: `main`
- Acceso: solo el Owner (Raoul Bermudez) tiene permisos de push.
- Los agentes pueden proponer commits pero no hacen push autónomo sin aprobación (Zona Amarilla per `RISK-POLICY.md`).

---

## 4. Google Drive

- Solo se sincronizan las carpetas definidas en `FOLDER-ARCHITECTURE.md §10.3`:
  - `01-inbox/01-owner-to-raul/`
  - `01-inbox/02-deliverables-to-owner/`
  - `02-knowledge-base/`
- El resto del repo (`04-system/`, `03-projects/`, `.claude/`) **no se sube a Drive**.
- Los agentes no modifican la configuración de Drive Desktop sin instrucción explícita del Owner.

---

## 5. InboxBot y automatizaciones externas

- El trigger activo (`trig_01RgGGbpCvckUzSwkyGMDNtm` — legado, pendiente Fase 4) solo crea borradores de Gmail; no envía correos directamente.
- Cualquier cambio de trigger, frecuencia o rutas es Zona Roja (ver `RISK-POLICY.md`).
- Los borradores generados por InboxBot deben revisarse antes de enviarse.

---

## 6. Uso de LLMs y datos del sistema

- Los archivos del repo pueden pasarse a LLMs como contexto de trabajo — son de naturaleza operativa/técnica.
- **Excepción:** no pasar a LLMs externos información de clientes, contratos confidenciales, o datos sensibles de terceros que puedan estar en inbox o proyectos.
- Perplexity, ChatGPT y equivalentes son herramientas de investigación; el conocimiento resultante se compila en `/RAUL/` en formato vendor-neutral.

---

## Notas de versión

- **v1.0 — 2026-04-25** — documento inicial.
