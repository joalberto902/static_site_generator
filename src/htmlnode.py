class HTMLNode:
    def __init__(
        self,
        tag: str | None = None,
        value: str | None = None,
        children: list["HTMLNode"] | None = None,
        props: dict[str, str] | None = None,
    ) -> None:
        self.tag: str | None = tag
        self.value: str | None = value
        self.children: list["HTMLNode"] | None = children
        self.props: dict[str, str] | None = props

    def to_html(self):
        raise NotImplementedError("to_html function is not implemented in the HTMLNode class")

    def props_to_html(self) -> str:
        if not self.props:
            return ""
        return (
            "".join(f' {key}="{val}"' for key, val in self.props.items())
        )
    def __eq__(self, other: object, /) -> bool:
        if not isinstance(other, HTMLNode):
            raise ValueError(f"{type(other)} can not be compared with HMTLNode")
        return (
            self.tag == other.tag
            and self.value == other.value
            and self.children == other.children
            and self.props == other.props
        ) 
    def __repr__(self) -> str:
        return f"""
        HTMLNode(
        {self.tag},
        {self.value},
        {self.children},
        {self.props_to_html()}
        )
        """


class LeafNode(HTMLNode):
    def __init__(
        self, 
        tag: str | None,
        value: str , 
        props: dict[str, str] | None = None
    ) -> None:
        super().__init__(tag=tag, value=value,props=props)

    def to_html(self) -> str:
        if self.value is None:
            raise ValueError("All LeafNode instances must have values")
        if self.tag is None:
            return self.value
        
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
    def __repr__(self) -> str:
        return f"""
        HTMLNode(
        {self.tag},
        {self.value},
        {self.props_to_html()}
        )
        """
    


class ParentNode(HTMLNode):
    def __init__(
        self,
        tag: str ,
        children: list["HTMLNode"] ,
        props: dict[str, str] | None = None
    ) -> None:
        super().__init__(tag = tag,children= children,props= props)

    def to_html(self) -> str:
        if self.tag is None:
            raise ValueError("All instances of ParentNode must have tags")
        if self.children is None:
            raise ValueError("All instances of ParentNode must have children")

        final_middle_string = ""
        for child in self.children:
            final_middle_string += child.to_html()
        return f"<{self.tag}{self.props_to_html()}>{final_middle_string}</{self.tag}>"
    def set_children(self, children: HTMLNode | list[HTMLNode]):
        if isinstance(children, HTMLNode):
            self.children.append(children) #type: ignore
            return 

        self.children.extend(children)#type: ignore


















