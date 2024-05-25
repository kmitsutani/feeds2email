systemd_unit_tmpl="""
""".strip()

systemd_timer_tmpl="""
""".strip()

default_config = dict(
)

systemd_unit = systemd_unit_tmpl.format(**default_config)
systemd_timer = systemd_timer_tmpl.format(**default_config)
