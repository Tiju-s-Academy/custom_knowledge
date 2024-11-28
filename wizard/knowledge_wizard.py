from odoo import models, fields


class KnowledgeArticleCoverWizard(models.TransientModel):
    _name = 'knowledge.wizard'
    _description = 'Upload Cover Image Wizard'

    cover_image = fields.Image(string="Cover Image")

    def action_set_cover_image(self):
        # Set the uploaded cover image to the article
        article_id = self.env.context.get('active_id')
        if article_id:
            article = self.env['knowledge.article'].browse(article_id)
            article.cover_image = self.cover_image