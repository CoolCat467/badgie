from dataclasses import dataclass


@dataclass(frozen=True)
class Project:
    type: str
    host: str
    full_path: str
    default_branch: str
    web_url: str


@dataclass(frozen=True)
class Badge:
    project_url: str
    project_ref: str

    def get_badge_image_url(self):
        raise NotImplementedError

    def get_link_title(self):
        try:
            return self.link_title
        except AttributeError:
            return ""

    def get_link_url(self):
        return self.project_url

    def get_markdown(self):
        return f"[![{self.get_link_title()}]({self.get_badge_image_url()})]({self.get_link_url()})"
