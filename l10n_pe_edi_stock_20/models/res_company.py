from odoo import fields, models


class ResCompany(models.Model):
    _inherit = "res.company"

    l10n_pe_edi_stock_client_id = fields.Char(
        string="Client ID",
        groups="base.group_erp_manager",
        help="Client ID assigned for the SUNAT delivery guide API.",
    )
    l10n_pe_edi_stock_client_secret = fields.Char(
        string="Client Secret",
        groups="base.group_erp_manager",
        help="Client Secret assigned for the SUNAT delivery guide API."
    )
    l10n_pe_edi_stock_client_username = fields.Char(
        string="Guide SOL User",
        groups="base.group_erp_manager",
        help="Username assigned for the SUNAT delivery guide API.",
    )
    l10n_pe_edi_stock_client_password = fields.Char(
        string="Guide SOL Password",
        groups="base.group_erp_manager",
        help="Password assigned for the SUNAT delivery guide API."
    )
    # Technical field to store the temporary token
    l10n_pe_edi_stock_token = fields.Char(groups="base.group_system")
