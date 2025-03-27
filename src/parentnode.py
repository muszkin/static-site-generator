from htmlnode import HTMLNode


class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if self.tag is None:
            raise ValueError("ParentNode must have a tag")
        if len(self.children) == 0:
            raise ValueError("ParentNode must have children")
        props = self.props_to_html()
        children = "".join([child.to_html() for child in self.children])
        if props:
            return f"<{self.tag} {props}>{children}</{self.tag}>"
        return f"<{self.tag}>{children}</{self.tag}>"

    def __repr__(self):
        return f"ParentNode({self.tag}, {self.children}, {self.props})"

    def __eq__(self, other):
        return self.tag == other.tag and self.children == other.children and self.props == other.props
