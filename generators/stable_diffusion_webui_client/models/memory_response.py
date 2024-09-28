from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.memory_response_cuda import MemoryResponseCUDA
    from ..models.memory_response_ram import MemoryResponseRAM


T = TypeVar("T", bound="MemoryResponse")


@_attrs_define
class MemoryResponse:
    """
    Attributes:
        ram (MemoryResponseRAM): System memory stats
        cuda (MemoryResponseCUDA): nVidia CUDA memory stats
    """

    ram: "MemoryResponseRAM"
    cuda: "MemoryResponseCUDA"
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        ram = self.ram.to_dict()

        cuda = self.cuda.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "ram": ram,
                "cuda": cuda,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.memory_response_cuda import MemoryResponseCUDA
        from ..models.memory_response_ram import MemoryResponseRAM

        d = src_dict.copy()
        ram = MemoryResponseRAM.from_dict(d.pop("ram"))

        cuda = MemoryResponseCUDA.from_dict(d.pop("cuda"))

        memory_response = cls(
            ram=ram,
            cuda=cuda,
        )

        memory_response.additional_properties = d
        return memory_response

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
