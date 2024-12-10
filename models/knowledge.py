from odoo import api, models, fields,_
from odoo.exceptions import ValidationError
from odoo.addons.web_editor.tools import get_video_embed_code, get_video_thumbnail
import base64


class KnowledgeArticle(models.Model):
    _name = 'knowledge.article'
    _description = 'Knowledge Article'

    name = fields.Char(string='Title', required=True)
    body = fields.Html(string='Content',)

    cover_image = fields.Binary(string="Cover Image", store=True)

    department_id = fields.Many2one('hr.department', string="Department")
    tag_ids = fields.Many2many('knowledge.tag', string="Tags")
    icon = fields.Binary(string="Icon", attachment=True, help="Upload an icon image")
    author_id = fields.Many2one('res.users', string='Author', default=lambda self: self.env.user)
    date_published = fields.Date(string='Published Date', default=fields.Date.context_today)

    image_1920 = fields.Image()
    video_url = fields.Char('Video URL',
                            help='URL of a video for showcasing your product.')
    embed_code = fields.Html(compute="_compute_embed_code", sanitize=False)

    attachments_ids = fields.Many2many(
        'ir.attachment',
        string="Attachments",
        help="Attach files like PDF, XLS, and PPT."
    )

    @api.onchange('video_url')
    def _onchange_video_url(self):
        if not self.image_1920:
            thumbnail = get_video_thumbnail(self.video_url)
            self.image_1920 = thumbnail and base64.b64encode(thumbnail) or False

    @api.depends('video_url')
    def _compute_embed_code(self):

        for image in self:
            image.embed_code = get_video_embed_code(image.video_url) or False

    @api.constrains('video_url')
    def _check_valid_video_url(self):
        for image in self:
            if image.video_url and not image.embed_code:
                raise ValidationError(
                    _("Provided video URL for '%s' is not valid. Please enter a valid video URL.", image.name))

    def action_add_cover(self):
        return {
            'type': 'ir.actions.act_window',
            'name': _('Add Cover Image'),
            'res_model': 'knowledge.wizard',
            'target': 'new',
            'view_mode': 'form',
        }

    def action_add_cover_video(self):
        return {
            'type': 'ir.actions.act_window',
            'name': _('Add Cover Video'),
            'res_model': 'knowledge.video.wizard',
            'target': 'new',
            'view_mode': 'form',
        }



