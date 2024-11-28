from odoo import fields, models


class KnowledgeVideoWizard(models.TransientModel):
    _name = 'knowledge.video.wizard'

    video_url = fields.Char('Video URL',
                            help='URL of a video for showcasing your product.')

    def action_set_cover_video(self):
        # Set the uploaded cover video to the article
        article_id = self.env.context.get('active_id')
        if article_id:
            article = self.env['knowledge.article'].browse(article_id)
            article.video_url = self.video_url
